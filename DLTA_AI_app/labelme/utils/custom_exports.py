# Don't Modify These Lines
# =========================================
custom_exports_list = []

# custom export class blueprint
class CustomExport:
    """
    A blueprint for defining custom exports.

    Attributes:
        file_name (str): The name of the file to export to.
        button_name (str): The name of the button that triggers the export.
        format (str): The format of the exported file.
        function (callable): The function that generates the export data.
        mode (str): The mode of the export, either "video" or "image".

    Methods:
        __call__(*args): Calls the function with the given arguments and returns the result.
    """
    def __init__(self, file_name, button_name, format, function, mode = "video"):
        """
        Initializes a new instance of the CustomExport class.

        Args:
            file_name (str): The name of the file to export to.
            button_name (str): The name of the button that triggers the export.
            format (str): The format of the exported file.
            function (callable): The function that generates the export data.
            mode (str): The mode of the export, either "video" or "image".
        """
        self.file_name = file_name
        self.button_name = button_name
        self.format = format
        self.function = function
        self.mode = mode

        custom_exports_list.append(self)
    
    def __call__(self, *args):
        """
        Calls the function with the given arguments and returns the result.

        Args:
            *args: The arguments to pass to the function.

        Returns:
            The result of calling the function with the given arguments.
        """
        return self.function(*args)
    
# =========================================


# Add your functions here ()
""" These functions must be divided as following:

1- helper functions: functions that are used by other functions and are not exported, no restrictions on them at all

Example: foo() in the dummy functions below.

2- exported functions (video): functions that are exported (video mode only):
they take the following arguments:
    results_file (str): Path to the JSON file containing the object detection results.
    vid_width (int): Width of the video frames.
    vid_height (int): Height of the video frames.
    annotation_path (str): Path to the output COCO annotation file.

and return annotation_path (str): to check if the function is working properly.

Example: bar() in the dummy functions below.

3- exported functions (image/dir): functions that are exported (image and dir mode * including video as frames *):
they take the following arguments:
    json_paths (list): List of paths to the JSON files containing the object detection results.
    annotation_path (str): The path to the output file.

and return annotation_path (str): to check if the function is working properly.

Example: baz() in the dummy functions below.    

** WARINING: All EXPORT FUNCTIONS MUST HAVE THE SAME ARGUMENTS OR ELSE THEY WILL NOT WORK. **

It's recommended to check `exports.py` file to see how the functions are called

"""
# =========================================
# dummy functions for testing
def foo():
    print("foo")

def bar(results_file, vid_width, vid_height, annotation_path):
    foo()
    print("bar")
    print(f"Export Function Check: results_file: {results_file} | vid_width: {vid_width} | vid_height: {vid_height} | annotation_path: {annotation_path}")

    return annotation_path

def baz(json_paths, annotation_path):
    foo()
    print("baz")
    print(f"Export Function Check: json_paths {json_paths} | annotation_path: {annotation_path}")

    return annotation_path


def count_objects(json_paths, annotation_path):
    import matplotlib.pyplot as plt
    import json

    labels = []
    counts = []
    # Loop through each JSON file
    for i in range(len(json_paths)):
        with open(json_paths[i]) as f:
            labels.append(json_paths[i].split("time_")[-1].split(".")[0].replace("_", ":")[-5:])
            # Load the JSON data
            data = json.load(f)
            inner_count = 0
            for j in range(len(data["shapes"])):
                inner_count += 1
            counts.append(inner_count)
        
        # Plot the counts
        plt.figure(figsize=(20, 12))
        plt.plot(counts)
        plt.title("Number of Objects Over Time")
        plt.tight_layout(pad=3)
        plt.grid()
        plt.xticks(range(len(labels)), labels, rotation=90)
        plt.yticks(range(max(counts)+1))
        plt.xlabel("Time")
        plt.ylabel("Number of Objects")
        plt.savefig(annotation_path)
        plt.close()
    
    return annotation_path
                
# =========================================


# create your custom exports here
# =========================================

# dummy exports for testing
# CustomExport("file_name", "video test1", "format", bar, "video")
# CustomExport("file_name", "image test1", "format", baz, "image")
CustomExport("plot_counts", "Plot Counts", "png", count_objects, "image")





# =========================================
