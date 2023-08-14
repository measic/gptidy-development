img_root = "img_align_celeba/resized_celebA/"
IMAGE_RESIZE = 64
batch_size = 128
use_cuda = torch.cuda.is_available()

data_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
])
dataset = datasets.ImageFolder(root=img_root, transform=data_transform)
