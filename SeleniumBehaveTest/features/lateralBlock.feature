# Created by IgorSenkiv at 20/09/2019
Feature: check lateral menu when the user has already logged

   Scenario: login in one step
    Given set up url address "login/index.php" and execute log in


  Scenario: user check if the right sidebar is accessible and navigable
    Given set up url address "login/index.php" and execute log in
    When user clicks on the button on the right corner of the sidebar to close and reopen it
    And scroll down the right sidebar
    And scroll down the content of the page
    Then the sidebar and content of the page should be scrolled

