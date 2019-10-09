# Created by IgorSenkiv at 03/10/2019
Feature: Check Top Navigation bar on the home page

  Scenario: check if ink of the dashboard has been returned Home Page
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the "Dashboard"
    Then Dashboard should returned home page "et.erickson.it: Expert Teacher"

  Scenario: check if link of the logo has been returned home page
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the "Logo Totara"
    Then after click on should be returned "Logo Totara"

  Scenario: check if ink of the Media Library has been returned  Shell ET - Media library integrata on new card
  of the browser
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the "Media Library"
    Then after click on should be returned "SHELL ET" on the new card of browser

   Scenario: check if link of the Curriculum Formativo is accessible
  and return Curriculum Formativo: Tutte Le Palestre
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the "Curriculum Formativo"
    Then after click on should be returned "Curriculum Formativo: Tutte Le Palestre"

  Scenario: check if the menu messaggi is accessible
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the item an anvelop "Menu messaggi"
    And clicks again on the item an envelope
    Then "menu messaggi" should be closed