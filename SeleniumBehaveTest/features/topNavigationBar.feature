# Created by IgorSenkiv at 03/10/2019
Feature: Check Top Navigation bar on the home page

  Scenario: check if ink of the dashboard has returned Home Page
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the Dashboard
    Then should be back on the page of my Dashboard "et.erickson.it: Expert Teacher"

  Scenario: check if link of the logo has returned home page
    Given set up url address "login/index.php" and execute log in
    When user clicks on the Expert Teacher logos on the upper left part
    Then should be back on the page of my Dashboard "et.erickson.it: Expert Teacher"

#
  Scenario: check if link of the Media Library has returned Shell ET - Media library integrata on the new card
  of the browser
    Given set up url address "login/index.php" and execute log in
    When user navigates on top navigation bar and click on the "Media Library"
#    Then after click on should be returned "SHELL ET" on the new card of browser
#
#   Scenario: check if link of the Curriculum Formativo is accessible
#  and has returned Curriculum Formativo: Tutte Le Palestre
#    Given set up url address "login/index.php" and execute log in
#    When user navigates on top navigation bar and click on the "Curriculum Formativo"
#    Then after click on should be returned "Curriculum Formativo: Tutte Le Palestre"
#
#  Scenario: check if the message menu is accessible
#    Given set up url address "login/index.php" and execute log in
#    When user navigates on top navigation bar and click on the item an anvelop "Menu messaggi"
#    And clicks again on the item an envelope
#    Then "menu messaggi" should be closed
#
#  Scenario: check if the notification menu is accessible
#    Given set up url address "login/index.php" and execute log in
#    When user navigates on top navigation bar and click on the item bell "Notifiche"
#    And clicks again on the item bell
#    Then "menu notifiche" should be closed
#
#  Scenario: check if the user's profile menu is accessible
#    Given set up url address "login/index.php" and execute log in
#    When user navigates on top navigation bar and click on the user's own name
#    And clicks again on the user's own name
#    Then user's menu profile "menu-content" should be closed