import os
from django.shortcuts import render
from django.http import HttpResponseRedirect

def processorSample(path_q, path_d):
    return "Path to queries is: {}, <br> Path to database is: {}".format(path_q, path_d)

def create_videos_page():
    answer = "<h2> Queries videos: </h2><br>"
    # Queries part

    for dirpath, dirnames, files in os.walk("queries_videos"):
        for file in files:
            path = "/static/" + file
            answer += "<div>"
            answer += "<h4> " + "Video file name: " + file + " </h4>"
            answer += "<a href = \"" + path + "\" download> Link to video </a><br>"
            answer += "<input type=\"checkbox\" name=\"" + file + "\" value=\"delete\" /> Delete this video <br>"
            answer += " </div><br>"

    answer += "<h2> Database videos: </h2><br>"
    # Database part

    for dirpath, dirnames, files in os.walk("database_videos"):
        for file in files:
            path = "/static/" + file
            answer += "<div>"
            answer += "<h4> " + "Video file name: " + file + " </h4>"
            answer += "<a href = \"" + path + "\" download> Link to video </a><br>"
            answer += "<input type=\"checkbox\" name=\"" + file + "\" value=\"delete\" /> Delete this video <br>"
            answer += " </div><br>"

    return answer

def handle_uploaded_file(f, type_of_file):
    source_name = f.name
    directory = ""
    if type_of_file == "database":
        directory = "database_videos/"
    else:
        directory = "queries_videos/"

    with open(directory + source_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# Delete the videos from file system if they were chosen by user to delete
def delete_videofiles(request):
    files_with_paths = {}

    for dirpath, dirnames, files in os.walk("queries_videos"):
        for file in files:
            files_with_paths[file] = os.path.join(dirpath, file)

    for dirpath, dirnames, files in os.walk("database_videos"):
        for file in files:
            files_with_paths[file] = os.path.join(dirpath, file)

    for filename in files_with_paths:
        if (request.POST.get(filename) == "delete"):
            os.remove(files_with_paths[filename])



def reconstruct_the_txt_files():
    path_to_queries = "queries.txt"
    path_to_database = "database.txt"

    # Remove old files
    if os.path.isfile(path_to_queries):
        os.remove(path_to_queries)

    if os.path.isfile(path_to_database):
        os.remove(path_to_database)

    # Queries part
    f = open(path_to_queries, "w+")
    counter = 0

    for dirpath, dirnames, files in os.walk("queries_videos"):
        counter = 0
        for file in files:
            f.write("q_" + str(counter) + "_" + file + "\t" + os.path.join(dirpath, file) + "\n")
            counter += 1
    f.close()

    # Database part
    f = open(path_to_database, "w+")
    counter = 0

    for dirpath, dirnames, files in os.walk("database_videos"):
        counter = 0
        for file in files:
            f.write("d_" + str(counter) + "_" + file + "\t" + os.path.join(dirpath, file) + "\n")
            counter += 1
    f.close()
