# Created by IgorSenkiv at 03/10/2019
Feature: Check Top Navigation bar on the home page

  Scenario: check if ink of the dashboard has returned Home Page
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user navigates on top navigation bar and click on the Dashboard
    Then should be back on the page of my Dashboard "et.erickson.it: Expert Teacher"

  Scenario: check if link of the logo has returned home page
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user clicks on the Expert Teacher logos on the upper left part
    Then should be back on the page of my Dashboard "et.erickson.it: Expert Teacher"

  Scenario: check if link of the Media Library is accessible and has returned Shell ET - Media library integrata
  on the new card of the browser
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user navigates on top navigation bar and clicks on the "Media Library"
    Then should be return the title of the page "SHELL ET"

  Scenario: check if link of the Curriculum Formativo is accessible and has returned Curriculum Formativo: Tutte Le Palestre
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user navigates on the top navigation bar and clicks on the "Curriculum Formativo"
    Then should be return the title of the page "Curriculum formativo"

  Scenario: check if the user'smessage menu is accessible
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user clicks on "an envelope item" that open and close "Menu messaggi"
    Then message menu should be closed

  Scenario: check if user's notification menu is accessible
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user navigates on top navigation bar click on the bell item that expand and close notification menu
    Then "menu notifiche" should be closed

  Scenario: check if appear user's menu when click on the user text name
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When user navigates on top navigation bar clicks on the user's text name
    Then "user's menu" should open