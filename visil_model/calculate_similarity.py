import json
import argparse
import tensorflow as tf
import os

from tqdm import tqdm
from visil_model.model.visil import ViSiL
from visil_model.datasets import VideoGenerator

def do_computations(query_file, database_file, output_file = 'result/results.json',
                    network = 'resnet', model_dir = 'visil_model/ckpt/resnet',
                    similarity_function = 'chamfer', batch_sz = 128,
                    gpu_id = 0, load_queries = False, threads = 8):
    # Create a video generator for the queries
    enqueuer = tf.keras.utils.OrderedEnqueuer(VideoGenerator(query_file, all_frames='i3d' in network),
                                              use_multiprocessing=True, shuffle=False)
    enqueuer.start(workers=threads, max_queue_size=threads*2)
    generator = enqueuer.get()

    # Initialize ViSiL model
    model = ViSiL(model_dir, net=network,
                  load_queries=load_queries, gpu_id=gpu_id,
                  similarity_function=similarity_function,
                  queries_number=len(enqueuer.sequence) if load_queries else None)

    # Extract features of the queries
    queries, queries_ids = [], []
    pbar = tqdm(range(len(enqueuer.sequence)))
    for _ in pbar:
        frames, video_id = next(generator)
        features = model.extract_features(frames, batch_sz)
        queries.append(features)
        queries_ids.append(video_id)
        pbar.set_postfix(query_id=video_id)
    enqueuer.stop()
    model.set_queries(queries)

    # Create a video generator for the database video
    enqueuer = tf.keras.utils.OrderedEnqueuer(VideoGenerator(database_file, all_frames='i3d' in network),
                                              use_multiprocessing=True, shuffle=False)
    enqueuer.start(workers=threads, max_queue_size=threads*2)
    generator = enqueuer.get()

    # Calculate similarities between the queries and the database videos
    similarities = dict({query: dict() for query in queries_ids})
    pbar = tqdm(range(len(enqueuer.sequence)))
    for _ in pbar:
        frames, video_id = next(generator)
        if frames.shape[0] > 1:
            features = model.extract_features(frames, batch_sz)
            sims = model.calculate_similarities_to_queries(features)
            for i, s in enumerate(sims):
                similarities[queries_ids[i]][video_id] = float(s)
            pbar.set_postfix(video_id=video_id)
    enqueuer.stop()

    # Save similarities to a json file
    with open(output_file, 'w') as f:
        json.dump(similarities, f, indent=1)
