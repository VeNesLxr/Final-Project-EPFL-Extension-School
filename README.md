MY FINAL PROJECT

This is the final project I had to do to get the certificate from Extension School EPFL. 
It was to use the skills we learnt and to add some new features that we never saw.

A one or two sentence description of your project here.

    What does it do?
        - It is a web project which tracks my books collection and how many books I have

    What is the "new feature" which you have added that we haven't seen before?
        - Pie chart with the genre of the books 
        - Current date
    

Prerequisites

Did you add any additional modules that someone needs to install (for instance anything in Python that you pip install-ed)? List those here (if any).

pip install -U matplotlib


Project Checklist

    [x] It is available on GitHub.
    [x] It uses the Flask web framework. /y
    [x] It uses at least one module from the Python Standard Library other than the random module. Please provide the name of the module you are using in your app.
        Module name: render_template
    [x] It contains at least one class written by you that has both properties and methods. This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code.
        File name: my_library.py
        Line number(s): 89
    [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser./y
    [x] It uses modern JavaScript (for example, let and const rather than var). /y
    [x] It makes use of the reading and writing to a file feature. /y
    [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least one example of a conditional statement in your code. /y
        File name: script.js
        Line number(s): 70
        File name: my_library.py
        Line number: 25
    [x] It contains loops. Please provide below the file name and the line number(s) of at least one example of a loop in your code. /y
        File name: my_library.py
        Line number(s): 119
    [x] It lets the user enter a value in a text box at some point. This value is received and processed by your back end Python code. /y
    [x] It doesn't generate any error message even if the user enters a wrong input.
    [x] The code is fully documented using comments. /y
    [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.


Comments from the teacher:

Overall, your project fulfills all requirements, so well done! Please find below the points we discussed during the meeting.

    - Login and the "Welcome (back) username" message: A separate login page could be created as discussed.
    
    - Issue with the pie graph:
        It doesn't update correctly, i.e., it doesn't show the latest one (it uses the cached version). A problem might be that you should not use pyplot with flask; see here https://matplotlib.org/devdocs/gallery/user_interfaces/web_application_server_sgskip.html
        Overlapping labels. An option is to provide the legend in a separate box next to the chart.
    
    - Counter how many books are on the list: If books get removed, the     counter doesn't update accordingly.
    
    - Python:
        Imports: Please find more details on the different options to import modules/submodules in the documentation.
        Reusability: The get_books(), get_books_search(), and get_wish_list() functions are quite similar so they could be merged into one using arguments.
        An option to save objects is with the pickle module. The documentation might be a bit hard to read, so I'd recommend looking for examples online. The setup you have in your app is perfectly fine. :)
    - An option to make your app live on the internet is to deploy it to Heroku, which is free for personal projects. Please find details here https://www.heroku.com/pricing

Congratulations on your excellent project and completing the course! I hope you feel like you learned helpful things and you will continue your journey in programming.