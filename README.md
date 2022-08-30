# Home Expenses Tracker
[View the live project here](https://home-expenses-tracker87.herokuapp.com/)

Home Expenses Tracker is a command-line application that allows to set budgets and input basic home expenses such as bills, food, and car expenses throughout the year.
The application calculates the totals and compares them to budgets when set by the user or calculable.
The program's goal is to provide the user with an immediate understanding of essentials spendings and eventually to help better manage one's finances.
Home Expenses Tracker's target is young adults who just moved out from their parent's house and need to plan and manage their finances.
It also targets families with low incomes, who need to pay attention to any expense to stay within their budgets.

To test the application without values here is the [link to the spreadsheet](https://docs.google.com/spreadsheets/d/16d9rYHmNwyW3FMlEfA099DIhwE0__wkl2gUl_VtKcjY/edit?usp=sharing).
Bear in mind that the values in the food and car worksheet must be subsequential for the correct functioning of the app, and to visualize the totals correctly, at least one value must be input in one of the expense worksheets.

## FEATURES:

### Welcome Section:

 <img src ="readme-images/welcome.png">

- This first section greets the user with a welcome message and requests to enter a number to choose the operation to perform from the presented list.

<img src ="readme-images/welcome-complete.png">

- If budgets have been set for the current month, it also gives the user immediate information about spending and budgets.

<img src ="readme-images/welcome-incomplete.png">

- If only some budgets have been set for the current month, it also gives the user the available information and states the unavailable budgets.

<img src ="readme-images/welcome-invalid.png">

- If the input choice is not in the number range or not a number at all, the program displays a customized message error.

### Months Section:

<img src="readme-images/months.png">

- This section requests the user to enter a number to choose the month relative to the previously selected operation.
- This section is displayed if:
  - The first choice is to update an expense;
  - The first choice is to set a monthly budget;
  - The first choice is to view a total and the choice of Total Type Section is 1.

  <img src="readme-images/month-invalid.png">

- If the input choice is not in the number range or not a number at all, the program displays a customized message error.

### Input Section:

<img src="readme-images/input.png">

- This section requests the user to enter the expense value to be registered or the budget's value to be set.

<img src="readme-images/input-invalid.png">

- If the input choice is not a positive number, the program displays a customized message error.

### Feedback Section:

<img src="readme-images/feedback.png">

- In this section, the program sends feedback to the user explaining how it handles the input data by printing the worksheet updated, the month, and the new value. Updating a value also triggers an update of monthly and yearly totals; messages of the main steps of the operations are displayed here too.

### Budget Section:

<img src="readme-images/budget.png">

- This section shows messages about the comparison between
monthly and yearly expenses and their respective budgets.

<img src="readme-images/budget-imp.png">

- If the comparison is not possible, another sentence explains the reason on the terminal.
- The Total Expenses budget can be set or calculated; if it's set, the value doesn't necessarily need to be the same as the sum of the other budgets.
- This section is displayed if:
  - The first choice is to update an expense;
  - The first choice is to set a monthly budget.

### Restart/Leave Section:

<img src="readme-images/restart.png">

- In this section, the program requests the user to choose between exiting the app or restarting the program.

<img src="readme-images/restart-invalid.png">

- If the input choice is: a letter but not y or n, not a letter at all, or more than one letter, the program displays a customized message error.

### Expense Type Section:

<img src="readme-images/expense-type.png">

- In this section, the program requests to enter a number to choose the expense type.
- This section is displayed if:
  - The first choice is to set a monthly budget;
  - The first choice is to view a total and the choice of Total Type Section is 2.

<img src="readme-images/expense-type-invalid.png">

- If the input choice is not in the number range or not a number at all, the program displays a customized message error.

### View Total Section:

<img src="readme-images/total.png">

- In this section, the program requests to choose which total to display: the total of expenses by month or the total of a specific expense type by year.

<img src="readme-images/total-invalid.png">

- If the input choice is not in the number range or not a number at all, the program displays a customized message error.

## Flowchart:

<img src="readme-images/chart.png">

## Testing:

<table>
<thead>
<tr>
<th>Action or Event</th>
<th>Expected Result</th>
<th>Successful?<th>
</tr>
</thead>
<tbody>
<tr>
<td>Run the program</td>
<td>Show welcome message and request of operation to execute</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number, not in the options range or a non-number</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>To update a worksheet: type a number between 1 and 7</td>
<td>Access to month options</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number between 1 and 12</td>
<td>Request the value of the expense</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number less than 0 or a non-number</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter valid data</td>
<td>- Update the relevant worksheet and inform the user;<br>
    - If the entry is of a monthly bill, only one value per month will be allowed;<br>
    - If the entry is for car or food expenses, it's possible to add more values for the same month;<br>
    - Update the monthly total of the selected expense in the total worksheet and inform the user;<br>
    - Update Year Total in the total worksheet and inform the user;<br>
    - Access the monthly budget for the selected expense and compare it to the respective total by sending a message to the user;<br>
    - State the difference between monthly budget and total;<br>
    - If the value for the monthly budget is not present, inform the user;<br>
    - Access the yearly budget for the selected expense and compare it to the respective total by sending a message to the user;<br>
    - If the value for the yearly budget is not present, try to calculate it.<br>If calculation is not possible due to missing information, inform the user
    - State the difference between yearly budget and total;<br>
    - Request to exit the game or continue with a new operation.
</td>
<td>Yes</td>
</tr>
<tr>
<td>Type "y"</td>
<td>Restart the program</td>
<td>Yes</td>
</tr>
<tr>
<td>Type "n"</td>
<td>Exit the program</td>
<td>Yes</td>
</tr>
<td>Type anything else</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>To set a monthly budget: type 8</td>
<td>Access to expense type options</td>
<td>Yes</td>
</tr>
<tr>
<td>Type a number not in the options range or a non-number</td>
<td>- Error message appears without stopping the program<br>
- Request again a valid input</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter valid number</td>
<td>Access to month options</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter valid number</td>
<td>Request relevant budget input</td>
<td>Yes</td>
</tr>
<tr>
<td>Enter budget data</td>
<td>- Update budget worksheet and inform the user;<br>
    - Access the monthly total for the selected expense and compare it to the respective budget by sending a message to the user;<br>
    - State the difference between monthly budget and total;<br>
    - Access the yearly budget for the selected expense and compare it to the respective total by sending a message to the user;<br>
    - If the value for the yearly budget is not present, try to calculate it.<br>- If calculation is not possible due to missing information, inform the user;<br>
    - State the difference between yearly budget and total;<br>
    - Request to exit the game or continue with a new operation.</td>
<td>Yes</td>
</tr>
<tr>
<td>To view totals: type 9</td>
<td>Access to total type options: by month or by expense type</td>
<td>Yes</td>
</tr>
<tr>
<td>Type 1</td>
<td>Access to month option</td>
<td>Yes</td>
</tr>
<tr>
<td>Select month number</td>
<td>- Print a message with the total of the expenses for the relevant month;<br>- Request to exit the game or continue with a new operation.</td>
<td>Yes</td>
</tr>
<tr>
<td>Type 2</td>
<td>Access to expense type options</td>
<td>Yes</td>
</tr>
<tr>
<td>Type expense type number</td>
<td>- Print a message with the yearly total of the selected expense type;<br>- Request to exit the game or continue with a new operation.</td>
<td>Yes</td>
</tr>
<tr>
</tbody>
</table>

### Validator Testing:
- PEP8 
No errors were returned when passing through the official [PEP8 validator](http://pep8online.com/);

## Bugs:
The initial idea was to create a worksheet for every expense.
When looping through the values of numerous worksheets, the program would have raised a 429 "Too many requests" error.
Reducing the number of worksheets fixed the problem.

When calculating the monthly bill totals, if there was an empty cell in the column, the program would have raised an int() error since "" can't be converted into an integer. 
Fill up all cells with 0 values temporarily fixed the error.
Adding a ternary operator in the function to convert to 0 all empty strings fixed the problem.

Opening the application in a month that didn't have values in the total or budget worksheet caused the program to break.
I reviewed the code and realized that the ValueError in the choose worksheet function wasn't the only potential error: there could also be an IndexError that I hadn't foreseen.
I modified the choose worksheet function by adding a try statement in the main one. This change handles problems caused by missing values in the total and budget worksheet and avoids program breaking.

## Deployment:
- In GitHub, create a list of requirements in requirements.txt by using this command in the terminal: **pip3 freeze > requirements.txt**;
- Commit and push these changes;
- Create an account on [Heroku](https://www.heroku.com/):
  - On the homepage, click sign-up and fill out the form;
  - Click **Create free account**;
  - Click the link provided in the confirmation email sent by Heroku;
  - Set a password and login;
  - Proceed and accept the terms of service;
- Click the **Create new app** button;
- Name your app by typing the chosen name under **App name**;
- Select your region and click the **Create app** button;
- On the menu bar, click on **Settings**;
- In the **Config Vars** section, click on **Reveal Config Vars**;
- In the field for **KEY** enter **CREDS**;
- Go back to the workspace, open creds.json, and copy the content;
- In the field for **VALUE** paste the creds.json file, and click **Add**;
- Add another Config Var underneath by entering **PORT** in the **KEY** field, **8000** in the VALUE field, and clicking the **Add** button;
- Scroll down to the **Buildpacks** section and click on **Add buildpack**;
- Select **Python** and click **Save changes**;
- Click on **Add buildpack** again, select **Node.js**, and click **Save changes**;
- Scroll up to the main menu bar and click on **Deploy**;
- In the **Deployment method** section, select **GitHub**;
- Click **Connect to GitHub**;
- Enter the name of your repository in the search bar and click **Search**;
- Once your repository it's shown underneath, click on **Connect**;
- Scroll down to the **Manual deploy** section;
- Click on **Deploy branch** making sure the branch to deploy is **main**;
- Wait until you see the message **Your app was successfully deployed**;
- Click on **View** to make sure your mock terminal is up and running.
  
## Credits:
- Code Institute's Love sandwiches walkthrough project: it helped to connect API, build the basic structure of my project and deploy it;
- [Ternary operator tutorial](https://www.tutorialspoint.com/ternary-operator-in-python): helped to solve the previously mentioned bug;
- [Get the month of a datetime](https://www.adamsmith.haus/python/examples/5639/datetime-get-the-year,-month,-and-day-of-a-%60datetime%60)
- [Grammarly](https://app.grammarly.com/): helped to correct grammar errors.

### Media:
[Lucidchart](https://www.lucidchart.com): used for the diagram in README.md

## Libraries:
[Gspread](https://docs.gspread.org):<br>used to access and update data in home-expenses-tracker spreadsheet;<br>
[Google auth](https://pypi.org/project/google-auth/):<br>it uses the creds.json file to set up the authentication needed  to access the Google Cloud project;
### Internal libraries:
Math: used (math.ceil) to round numbers up to the next largest integer;<br>
Datetime: used to show data relative to the current month.