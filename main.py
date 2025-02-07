import numpy as np
from skimage import io
import matplotlib.pyplot as plt

print("Welcome to Introduction to NumPY")

a = np.zeros(3) # Creates a array
print(a)
print(type(a))
print(type(a[0]))

z = np.zeros(10)
print(z)
print(type(z))
print(type(z[0]))

print(z.shape)

# z.shape = (10, 1)
# print(z)

z = np.ones(10)
print(z)
print(type(z))
print(type(z[0]))

z = np.empty(3)
print(z)
print(type(z))
print(type(z[0]))

z = np.linspace(2, 10, 5) # From 2 to 10, with 5 elements
print(z)
print(type(z))
print(type(z[0]))

z = np.array([10, 20])
print(z)
print(type(z))
print(type(z[0]))

a_list = [1,2,3,4,5,6,7]
z = np.array([a_list])
print(z)

b_list = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7],[1,3,5,7,9,2,4]]
z = np.array([b_list])
print(z)
print(z.shape)
# print(?z.shape)

np.random.seed(0)
z1 = np.random.randint(10, size=6)
print(z1)
print(z1[0])
print(z1[0:2])
print(z1[-1])

photo = io.imread('york_minister.jpg')
print(type(photo))
print(photo.shape)
print(plt.imshow(photo))
print(plt.imshow(photo[::-1]))   # Reversed Image (Row reversed)
print(plt.imshow(photo[:, :-1])) # Mirror Image   (Col reversed)
print(plt.imshow(photo[50:150, 150:280])) # Taking rows from 50 to 150 && Taking cols from 150 to 280
print(plt.imshow(photo[::2, ::2]))  # Taking every other row and col (Halfed the size of the image)

print(photo)
photo_sin = np.sin(photo)
print(photo_sin)

print(np.sum(photo))
print(np.prod(photo))
print(np.mean(photo))
print(np.std(photo))
print(np.var(photo))
print(np.min(photo))
print(np.max(photo))
print(np.argmin(photo))
print(np.argmax(photo))

z = np.array([1, 2, 3, 4, 5])
print(z)
print(z < 3)
print(z > 3)
print(z[z > 3])

photo_masked = np.where(photo > 100, 255, 0)
print(plt.imshow(photo_masked))

a_array = np.array([0,1,2,3,4])
b_array = np.array([5,6,7,8,9])

print(a_array + b_array)
print(a_array + 30)
print(a_array * b_array)
print(a_array * 10)
print(a_array @ b_array)  # Dot product of these two arrays

print(plt.imshow(photo[:,:,0].T)) # Transposes the image

x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))

print("Completed!")
#https://www.youtube.com/watch?v=xECXZ3tyONo