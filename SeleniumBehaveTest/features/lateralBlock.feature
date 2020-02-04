# Created by IgorSenkiv at 20/09/2019
Feature: check right sidebar menu when the user has already logged

  Scenario: user check if the right sidebar is accessible and navigable
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user clicks on the button on the right corner of the sidebar to close and reopen it
    And scroll down the right sidebar
    And scroll down the content of the page
    Then the sidebar and content of the page should be scrolled