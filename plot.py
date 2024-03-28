# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches
import os

def filterFiles(directoryPath, extension):
    """
        This function filters the format files with the selected extension in the directory
        
        Args:
            directoryPath (str): relative path of the directory that contains text files
            extension (str): extension file

        Returns:
            The list of filtered files with the selected extension
    """    
    relevant_path = directoryPath
    included_extensions = [extension]
    file_names = [file1 for file1 in os.listdir(relevant_path) if any(file1.endswith(ext) for ext in included_extensions)]
    numberOfFiles = len(file_names)
    listParams = [file_names, numberOfFiles]
    return listParams

[image_names, numberOfFiles] = filterFiles("BCCD/JPEGImages", "jpg")    

trainRCNN = pd.read_csv('test.csv', sep=",", header=None)
trainRCNN.columns = ['filename', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax']
trainRCNN.head()
rbc=0

for imageFileName in image_names:    
    fig = plt.figure()
    #add axes to the image
    ax = fig.add_axes([0,0,1,1]) #adding X and Y axes from 0 to 1 for each direction 
    plt.axis('off')

    # read and plot the image
    image = plt.imread('BCCD/JPEGImages/' + imageFileName)
    plt.imshow(image)
    # iterating over the image for different objects
    for _,row in trainRCNN[trainRCNN.filename == imageFileName].iterrows():
        xmin = float(row.xmin)
        xmax = float(row.xmax)
        ymin = float(row.ymin)
        ymax = float(row.ymax)
        
        width = xmax - xmin
        height = ymax - ymin
        ClassName= row.cell_type
        # assign different color to different classes of objects
        if row.cell_type == 'RBC':
            ax.annotate('RBC', xy=(xmax-40,ymin+20))
            rbc = rbc + 1
            rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = 'r', facecolor = 'none')
        elif row.cell_type == 'WBC':
            ax.annotate('WBC', xy=(xmax-40,ymin+20))
            rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = 'b', facecolor = 'none')
        elif row.cell_type == 'Platelets':
            ax.annotate('Platelets', xy=(xmax-40,ymin+20))
            rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = 'g', facecolor = 'none')        
        else:
            print("nothing")
    
        ax.add_patch(rect)   
        if not os.path.exists("imagesBox"):
            os.makedirs("imagesBox")

        fig.savefig('imagesBox/' + imageFileName, dpi=90, bbox_inches='tight')
    plt.close()
    print("ImageName: " + imageFileName + " is saved in imagesBox folder")
    print(rbc)
        
print("PLOTBOX COMPLETED!")
        



# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import patches
# import os

# def filterFiles(directoryPath, extension):
#     relevant_path = directoryPath
#     included_extensions = [extension]
#     file_names = [file1 for file1 in os.listdir(relevant_path) if any(file1.endswith(ext) for ext in included_extensions)]
#     numberOfFiles = len(file_names)
#     listParams = [file_names, numberOfFiles]
#     return listParams

# def plot_boxes(image_path, df):
#     fig = plt.figure()
#     ax = fig.add_axes([0, 0, 1, 1])
#     plt.axis('off')

#     image = plt.imread(image_path)
#     plt.imshow(image)

#     # Create the imagesBox folder if it doesn't exist
#     if not os.path.exists("imagesBox"):
#         os.makedirs("imagesBox")

#     for _, row in df[df.filename == os.path.basename(image_path)].iterrows():
#         xmin = float(row.xmin)
#         xmax = float(row.xmax)
#         ymin = float(row.ymin)
#         ymax = float(row.ymax)

#         width = xmax - xmin
#         height = ymax - ymin
#         ClassName = row.cell_type

#         if row.cell_type == 'RBC':
#             ax.annotate('RBC', xy=(xmax - 40, ymin + 20))
#             rect = patches.Rectangle((xmin, ymin), width, height, edgecolor='r', facecolor='none')
#             ax.add_patch(rect)
#         elif row.cell_type == 'WBC':
#             ax.annotate('WBC', xy=(xmax - 40, ymin + 20))
#             rect = patches.Rectangle((xmin, ymin), width, height, edgecolor='b', facecolor='none')
#             ax.add_patch(rect)
#         elif row.cell_type == 'Platelets':
#             ax.annotate('Platelets', xy=(xmax - 40, ymin + 20))
#             rect = patches.Rectangle((xmin, ymin), width, height, edgecolor='g', facecolor='none')
#             ax.add_patch(rect)
#         else:
#             print("Unknown cell type:", row.cell_type)

#     fig.savefig('imagesBox/' + os.path.basename(image_path), dpi=90, bbox_inches='tight')
#     plt.close()
#     print("ImageName: " + os.path.basename(image_path) + " is saved in imagesBox folder")

# # Get user input for the image path
# user_image_path = input("Enter the path of the image for detection: ")

# # Read the CSV file
# trainRCNN = pd.read_csv('test.csv', sep=",", header=None)
# trainRCNN.columns = ['filename', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax']
# trainRCNN.head()

# # Call the function to plot boxes
# plot_boxes(user_image_path, trainRCNN)

# print("PLOTBOX COMPLETED!")






# C:/Users/NAMAN GATHANI/Desktop/Mini Project/archive/dataset-master/dataset-master/JPEGImages/BloodImage_00241.jpg
# C:\Users\NAMAN GATHANI\Desktop\miniproject2\BCCD\JPEGImages\BloodImage_00003.jpg
# BCCD\JPEGImages\BloodImage_00003.jpg