# Tutorial

## Introduction
The following section is a brief tutorial of Fixel. Here, we highlight key aspects of the language through example programs that demonstrate how users can build up functionality in their Fixel code. At its core, Fixel is a language for image editing. But given the right tools, it can be a powerful tool in automating the process of touching up and fixing images.

This tutorial will focus on the basics of the language—from built-in functions to primitive and derived types—and expands on how to use these tools in Fixel to construct powerful image filters. The basis for this language is the ability to customize and combine common image filters to generate unique image treatments that can then be reused as needed. The given examples demonstrate how to couple filters with input images to produce more visually interesting output images, and then to perform the same transformation on multiple images with relative ease. 

The Fixel language facilitates image editing and makes writing code for image processing more user-friendly. It aims to be human-readable, modular, and easy to learn, regardless of one's familiarity with other programming modalities. Its syntax is based on that of common social media services, and can easily be understood as sample conversations in these programs.


## Basic Functionality
Fixel is, at its core, an image processing language. We therefore begin by introducing how it deals with images, as illustrated by a few, very basic Fixel program.s

### Using Images
Before getting into the basic construction of Fixel programs, it is first necessary to address the use of images in Fixel. They serve as the foundation for any sort of image processing one might wish to test.

The purpose of Fixel is to create filters to edit images easily and efficiently. The language is used to write executable filters that can then be applied to an input image to produce an output image. Consequently, all Fixel programs are written with the purpose of modifying a given input image, or images.

The most minimal Fixel program would read as follows:

	blank.fxl
	
To run this program, the user executes the command:

	./fixel blank.fxl input-image.jpg
	
If all else is running fine, the program will execute on the input image and produce a new image file, `input-image-fixel.jpg` in the same directory. Running `blank.fxl` with an image will produce a copy of the input image. 

Memory for an image is dynamically allocated by the system at run time. At the moment, our sample program `blank.fxl` performs no transformations on any of the input images, it just spits out a duplicate of any and all images inputted into the program on execution. If we were to insert code that referenced the inputted images, it would perform transformations on the images, and the output images would contain those modifications. 

So how does one work with images? This is accomplished by creating an image using Fixel's `@image` syntax. Using the variable name image1, we can now access certain attributes of the image, namely width, height, file type, and color space. Let’s look at an example of this using one of Fixel's built-in functions, described in detail in later sections:

	#grayscale @image1
	------------
	gray.fxl

To run this program, the user executes the command:

	> ./fixel gray.fxl input-image.jpg

The result of this program is a new image file, input-image-fixel.jpg, which is a grayscale version of the image edited using one of Fixel's built-in functions, `#grayscale`. As seen in the preceding example, functions are called on images using the `#` to indicate a function name. This program simply defines a single input image (image1) for the Fixel program to work with, using the `@` symbol to define it as a variable. Image variables are sequentially declared by Fixel using this syntax, so the user does not need to explicitly declare them. 

Part of Fixel's appeal is its ability to work with multiple images within a single instance of a filter program. To perform an action on multiple images, simply stack them on top of on another and run functions on them:

	#grayscale @image0
	#grayscale @image1
	#grayscale @image2
	------------
	gray-multi.fxl

To run this program, the user executes the command:

	> ./fixel gray-multi.fxl image0.jpg image1.gif image2.png

This program will result in the three input images passed as arguments through the execution command being reproduced in grayscale, in the same directory as their original name with `-fixel` appended to the file name.

As can be seen from this execution command, for every image defined in a Fixel program, a separate argument needs to be appended to the execution command with the path of the input image.

Additionally, the images need not have the same file extension within a single Fixel program—so long as the files are of valid image format, they can be used with Fixel.

Variables can only be used to declare non-image types, like integers, strings, lists and so on. They also cannot use the syntax reserved for image variables (`image0`,`image1`, and so on). These variables may be of the types listed later in the Variables section of the Tutorial and in the accompanying Language Reference Manual.

### Hello World
Fixel's Hello World program takes an image as input and overlays the text "Hello, World!" over the photo. This program demonstrates using Fixel to manipulate an input image using one of Fixel's built-in functions, `#caption`.

	#caption @image0, "Hello, World!"
	------------
	hello-world.fxl

To run this program, the user executes the command:

	> ./fixel hello-world.fxl image0.jpg

The input and resulting output photos of this program are shown below:

![Single image being captioned by Fixel.](./img/tutorial1.png)

How does this program work? Let's deconstruct the single code statement made in `hello-world.fxl`.

The first word is the function call, denoted by the `#` symbol. Because `#caption` is a built-in function (which are described in detail in the next section) it needs no function definition. 

The next word, `@image0` refers to the input image, passed to the program during execution. The interpreter will throw an error during runtime if a program refers to `@image1` without passing in two input images.

The final aspect of the code statement is the string in quotes, "Hello, World!" The built-in function `#caption` takes in an argument, the string to be overlaid on the image. Arguments to a function are passed as comma-separated statements. If we wanted to overlay a different text with the `#caption` function, we could write:

	#caption @image0, "Hey!"

or

	#caption @image0, "?!?!!@()#$*#@"

to display different text on the image.

To further demonstrate the functionality presented in `hello-world.fxl`, let's caption multiple images in one Fixel program:

	#caption @image0, "Hello, World!"
	#caption @image1, "Hello, again."
	#caption @image2, "Hi!"
	------------
	hello-world-multi.fxl

We run this program by executing:

	> ./fixel hello-world-multi.fxl image0.jpg image2.jpg image3.jpg

The resulting images appear as follows:

![Multiple images being captioned by Fixel.](./img/tutorial2.png)

## Built-in Functions
One goal of Fixel is to allow the user to construct varied and complex image filters without the need for involved programming. This is partly enabled through the implementation of Fixel's built-in functions. Fixel comes with a number of built-in functions to assist the user in creating human-readable, accessible image filters, and allows the user to stack them to produce more interesting effects.

As seen in `hello-world.fxl`, functions are invoked using the `#` symbol. 

### Grayscale (a function without arguments)

	#grayscale @image0
	------------
	gray.fxl

Grayscale is a simple built-in function that converts an image to a grayscale image while still outputting a conventional RGB image.

### Overlay (a function with multiple arguments)

	#overlay @image0, color(255,0,0), 10
	------------
	red-overlay.fxl

Overlay allows the user to overlay an image with a color fill. The intensity of the fill can be modulated by the percentage argument, which specifies what opacity the fill is to be set at. An example of `red-overlay.fxl` in action can be seen below:

![`red-overlay.fxl` illustrates how to use the built-in overlay function.](./img/tutorial3.png)

### Full List of Built-in Functions
Presented here are basic instructions on how to call the functions built into Fixel on inputted images. For an explanation of what each of these functions does, please consult the white paper.

+ Grayscale — `#grayscale @image0`
+ Overlay — `#overlay @image0 [r,g,b],opacity`
+ Brightness — `#brighten @image0 percentage`
+ Contrast — `#contrast @image0 percentage`
+ Border — `#border @image0 size, color`
+ Crop — `#cropit @image0 coordinates`
+ Scale — `#scale @image0 percentage`
+ Collage — `#collage outputImage, listOfImages, width, height`
+ Rotate — `#rotate @image0 angle`
+ Caption — `#caption @image0 text`

## Primitives and Colors
Fixel supports the following primitive types: `int`, `double`, `boolean`, `string`, and `image` type. These are useful for using data (like dimensions) from one image to make changes to another.

Fixel also provides support for colors as a 3-integer tuple representation of an RGB value, created either with those RGB values, or a hex value (example: `#f0f0f0`), or a string identifying the color (example: `red`). Fixel also supports points as a 2-integer tuple representing a pixel location, and list structures. 

## Variables and Expressions
Fixel can also be used to read certain attributes of images and then use those values to modify other images passed into the program. This is done by reading these values into program variables and then manipulating them using using common arithmetic operators: `+`, `-`, `*`, and `/`.

Say, for instance, we'd like to write a program that takes two images with different dimensions and stretch or compress them to be double the height and width of a third image. In that case, our program would look like this:

	@desiredWidth = @image0.width*2
	@desiredHeight = @image0.height*2
	@imagesToStandardize = [@image1,@image2]

	for @currentImage in @imagesToStandardize:
			#stretch @desiredWidth, @desiredHeight, @currentImage
	------------
	standardizing-dimensions.fxl

`standardizing-dimensions.fxl` first instantiates variables for the three input images. It then reads the height and width of `image0` into variables called `desiredWidth` and `desiredHeight`, doubling the value immediately using the `*` operator. Next, it loads the images to standardize into a list variable and cycles through them using a `for` loop to stretch them to double the dimensions of `image0`. This could also be done without the `for` loop, but it is used here to illustrate a sample syntax for this kind of operation. `for` and `if` statements will be explored further in the "Control Flow" section.

We run this program by executing:

	> ./fixel standardizing-dimensions.fxl image0.jpg image1.jpg image2.jpg

The resulting images appear as follows:

![Output of the standardizing-dimensions.fxl program.](./img/tutorial4.png =250x)

This process can, of course, be extended to any of the image's attributes. It can also be used to dynamically determine input arguments for Fixel's colorization functions. We can, for instance, use a step function to output sequential images with incremental increases in opacity or redness.

## Building Custom Functions
Like most other programming languages, Fixel also allows users to group together and manipulate built-in functions to create custom ones. This is where the true power of Fixel lies—by empowering users with the ability to customize the filters they wish to apply to their images, they are no longer limited to the pre-determined combination of image transformations most image sharing applications offer them. 

Custom functions are easy to design and implement. They are defined by beginning a line with the `#` symbol, followed by a space, then the name of the function, followed by the variable names for the function's arguments (separated by a comma and an optional space), and finally a colon. This sequence of characters indicates to Fixel that we are about to define a function, rather than just call it on an image variable. We then add a line break, and stack the functions or statements we'd like the function to include in a tab-indented list.
 
Here's a sample program that first establishes a function that stretches an image to be the size of indicated by its input arguments, then converts it to grayscale and adds a caption that says `"Welcome to My Computer!"`:

	#generateWallpaper @image0, 1600, 1200

	generateWallpaper @imageName, @desktopWidth, @desktopHeight:
			#stretch @imageName, @desktopWidth, @desktopHeight
	#grayscale @imageName
	#caption @imageName, "Welcome to My Computer!"
	------------
	creating-wallpapers.fxl

We are first defining the function generateWallpaper and establishing that it has two input arguments: desktopWidth and desktopHeight. We then stack three built-in functions within `#generateWallpaper`. The first, `stretch`, passes the two input arguments as its own. The other two, `grayscale` and `caption` have static input arguments. Once we've defined our custom function, we then can apply it to `@image0` using the desired parameters (in this case, a width of `1600` and a height of `1200`).

We run this program by executing:

	> ./fixel creating-wallpapers.fxl image0.jpg

The resulting images appear as follows:

![Output of the generateWallpaper Fixel program.](./img/tutorial5.png)

## Control Flow
The Fixel language allows for two types of loops: `for` and `while` loops. In addition, users may employ `if` or `if...else` statements. The syntax for these loops is demonstrated in the following sections.

### `for` Loops
`for` loops in Fixel are written in the same way as in most other programming languages. It is especially useful for using the same set of transformation functions on a multitude of images at once. An example of how to use the for loop can be seen in `standardizing-dimensions.fxl` above.

`for` loops are formatted as such: `for`, followed by a space, then the condition (which can instantiate a variable to use to cycle through the elements of an array, as in `standardizing-dimensions.fxl`), followed by a colon, followed by a line break, followed by a tab-indented list of commands to execute.

### `while` Loops
Similarly, `while` loops can help users make incremental changes to photos as it processes them one by one. In this case, as long as the condition in the initial line holds true, the functions within the statement continue to be executed. For instance, say if we have a list of six images in the variable `@imagesList`, and we'd like their opacities to range from `40` to `100`, with each one's being ten percent higher than the previous one. In this case, we can create a `while` loop in our program like so:

	@imageCount = 0
	@currentOpacity = 0.4

	while @imageCount<6:
		#opacity @imagesList.imageCount, @currentOpacity
		@currentOpacity = @currentOpacity + .1
		imageCount++
	------------
	incremental-opacity.fxl

`while` loops are structured in almost the exact same way as `for` loops.

### `if` And `if...else` Statements
Fixel also supports the use of `if` and `if...else` statements to direct control flow. This can be used to apply special transformations to certain images based on their properties. For example, if we have a list of images in the variable `@imagesList` and we'd like to compress all images with a pixel width less than `200` to `200`, we can do so with the `minimum-width.fxl` program:

	for @currentImage in @imagesList:
		if @currentImage.width<200:
			@proportionalHeight = @currentImage.height*(200/@currentImage.width)
			#stretch @currentImage, 200, @proportionalHeight
	------------
	minimum-width.fxl

Here, the program is cycling through the images in `@imagesList` and checking to see if their width is less than `200`. If it is, then the program stretches them to have a width of `200` and retain a proportional height. In the same way, if we wanted the program to also standardize every image with a width above `200` to a width of `300`, we could use an `if...else` statement:

	for @currentImage in @imagesList:
		if @currentImage.width<200:
			@proportionalHeight = @currentImage.height*(200/@currentImage.width)
			#stretch @currentImage, 200, @proportionalHeight
		else:
			@proportionalHeight = @currentImage.height*(300/@currentImage.width)
			#stretch @currentImage, 300, @proportionalHeight
	------------
	minimum-maximum-width.fxl

Tab-indentation and line breaks hold the same amount of importance in `if` and `if...else` statements as in `while` and `for` loops.

## Conclusion				
This language tutorial for Fixel covers to core concepts for programming image processing filters, and will hopefully serve as a tool for users in getting started with the language. A more comprehensive analysis of the language's characteristics can be found in the Language Reference Manual, and a complete explanation of how the built-in functions work can be found in the white paper.
