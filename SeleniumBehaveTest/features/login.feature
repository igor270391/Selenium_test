# Created by IgorSenkiv at 16/09/2019________
Feature: Login feature

  Scenario: the user enters valid username and valid password on log in
    Given url address "login/index.php"
    When user enters a username "mt2k-adm"
    And user enters a password "MncQkSa5y_0LcoMdo"
    And click Login button
    Then I should have a title "et.erickson.it: Expert Teacher"


  Scenario: the user enters invalid username and invalid password on log in
    Given url address "login/index.php"
    When user enters a username "i.senkiv"
    And user enters a password "1q2w3e"
    And click Login button
    Then I should have a message "Login errato, riprova"


  Scenario: user changes the language in "English (en)"
    Given url address "login/index.php"
    When user navigate to drop down language menu
    And select English (en) language
    Then User should has the page log-in in "en" language

  Scenario: user execute logs out from portal erikson
    Given url address "login/index.php"
    When user enters a username "i.senkiv"
    And user enters a password "Totara_2019"
    And click Login button
    Then navigate to menu dropdown end click esc