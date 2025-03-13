from matplotlib import pyplot as plt

from K22416C.SAKILA_BAITAP.main import inertia

# Vẽ đồ thị Elbow
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Số cụm (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()