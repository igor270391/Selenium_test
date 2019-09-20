# Created by IgorSenkiv at 20/09/2019
Feature: check lateral menu when the user has already logged

   Scenario: login in one step
    Given set up url address "login/index.php"


  Scenario: user closes lateral menu for view home page in full screen
    Given set up url address "login/index.php"
    When click on the button of the lateral menu