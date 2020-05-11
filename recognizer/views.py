from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import render
# Create your views here.
from django.utils.safestring import mark_safe
from recognizer import mainLogic
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .mainLogic import handle_uploaded_file, reconstruct_the_txt_files, create_videos_page, delete_videofiles
from visil_model.calculate_similarity import do_computations


def index(request):
    return render(request, "index.html")

def do_smtnhg(request):
    path_quaries = request.POST.get("file_path_quaries")
    path_database = request.POST.get("file_path_database")
    new_path = mainLogic.processorSample(path_quaries, path_database)
    return render(request, "index.html", {"param": mark_safe(new_path)})

def show_all_videos(request):
    answer = create_videos_page()
    return render(request, "videos.html", {"param": mark_safe(answer)})

def go_somewhere(request):
    return render(request, "sample.html")

def delete_videos(request):
    if request.method == 'POST':
        delete_videofiles(request)
    # Reconstruct the model-related text files for the reason of deleting some videos
    reconstruct_the_txt_files()
    # Return to the videos page
    answer = create_videos_page()
    return render(request, "videos.html", {"param": mark_safe(answer)})

def show_results(request):
    #do_computations(query_file="queries.txt", database_file="database.txt")
    return render(request, "waiting.html")

def compute(request):
    do_computations(query_file="queries.txt", database_file="database.txt")
    answer = "<h2> Now you are able to download the results by clicking the link below. After it you can press the \"Return to home page\" button to return to the home page </h2><br>"
    path = "/static/" + "results.json"
    answer += "<a href = \"" + path + "\" download> Link to download the result JSON file </a><br>"
    return render(request, "waiting.html", {"param": mark_safe(answer)})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        files = request.FILES.getlist('video')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f, request.POST.get('type_of_video'))
            reconstruct_the_txt_files()
        return HttpResponseRedirect('/upload_file/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_f.html', {'form': form})
