import imageio.v3 as iio

filenames = ['AlienF1v2.png', 'AlienF2v2.png', 'AlienF3v2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('Alien_WBG.gif', images, duration = 500, loop = 0)
