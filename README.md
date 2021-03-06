# birthday_wishes_to_employees.
## Overview
A requirement exists at Realm Digital to develop a service component that will send birthday wishes to employees.
This practical assessment will allow the candidate to demonstrate that he/she fully understands the concepts
needed to write coherent software.
The solution should be simple but should demonstrate your understanding of software design concepts, and how to
create maintainable well-structured software.
We estimate this would take 2 or 4 hours to complete.
A technical lead will review your solution and the interview process will include discussion of your design and
implementation.
The Objective
Design and implement a service component that will send birthday wishes to employees.
The service must extract a list of employees whose birthdays occur today using the Realm Digital Employee API
and create a generic message E.g. “Happy Birthday {name 1}, {name 2}” and send the message to an email
address configured for the component.
The following needs to be considered:
● Leap years.
● Employee exclusions. An exclusion can be any of the following:
○ The employee no longer works for Realm Digital;
○ The employee has not started working for Realm Digital;
○ Or the employee has been specifically configured to not receive birthday wishes.

The component must support being executed at most once for a specific employee’s birthday wish, regardless of
how many times the service is scheduled to run on a specific day.
Architecturally, the solution must be designed to support additional messaging functionality such as sending work
anniversary messages.
Note: The work anniversary requirement does not need to be coded but the solution design should cater for the
additional requirement.
