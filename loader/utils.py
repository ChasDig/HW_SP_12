# 5: Func: save images by POST:
def picture_save(picture) -> str:

    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)

    return path
