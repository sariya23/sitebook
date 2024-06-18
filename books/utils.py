import uuid


def handle_upload_file(f):
    with open(f"uploads/{uuid.uuid4()}{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
