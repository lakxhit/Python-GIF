import imageio.v3 as iio
filenames = ['lak1.jpg', 'lak2.jpg']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
  iio.imwrite('lol.gif', images, duration = 500, loop = 0)
