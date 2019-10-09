# Created by IgorSenkiv at 03/10/2019
Feature: Check status of program
  Chose the nessecery button to filtered course

  Scenario: Check Incourse program
    Given set up url address "login/index.php" and execute log in
    When user clicks on
#    Then should be remain only the list of corses reffered to selected filter