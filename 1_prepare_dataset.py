import os


def make_folder(folder_path):
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)


if __name__ == '__main__':
    dataset_dir = '/Users/tia/Desktop/UE1_projet/dataset'
    test_dir = os.path.join(dataset_dir, 'test')
    demo_images_dir = os.path.join(test_dir, 'demo_images')
    images_dir = os.path.join(test_dir, 'images')
    videos_dir = os.path.join(test_dir, 'videos')

    make_folder(test_dir)
    make_folder(demo_images_dir)
    make_folder(images_dir)
    make_folder(videos_dir)

if __name__ == '__main__':
    dataset_train_dir = '/Users/tia/Desktop/UE1_projet/dataset_train'
    Annotations_dir = os.path.join(dataset_train_dir, 'Annotations')
    Images_dir = os.path.join(dataset_train_dir, 'Images')
    ImageSet_dir = os.path.join(dataset_train_dir, 'ImageSets')
    Main_dir = os.path.join(ImageSet_dir, 'Main')

    make_folder(dataset_train_dir)
    make_folder(Annotations_dir)
    make_folder(Images_dir)
    make_folder(ImageSet_dir)
    make_folder(Main_dir)