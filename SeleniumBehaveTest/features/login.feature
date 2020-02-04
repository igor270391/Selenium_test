# Created by IgorSenkiv at 16/09/2019________
Feature: Login feature

  Scenario: login with valid credentials
    Given url address "login/index.php"
    When type username "mt2k-adm"
    And type password "MncQkSa5y_0LcoMdo"
    And click on Login
    Then the title of the current page should be "et.erickson.it: Expert Teacher"


  Scenario: login with invalid credentials
    Given url address "login/index.php"
    When type username "mt2k-adm"
    And type password "MncQkSa5y_0LcoMd"
    And click on Login
    Then should appear the message "Login errato, riprova"


  Scenario: user changes the language in "English (en)"
    Given url address "login/index.php"
    When user navigate to drop down language menu
    And select English (en) language
    Then user's login page should be in "en"


  Scenario: user execute log out
    Given url address "login/index.php"
    When type username "i.senkiv"
    And type password "Totara_2019"
    And click on Login
    Then navigate to menu dropdown end click esci


  Scenario: login in one step with agreement privacy of E-Learning platform Erickson: Expert Teacher
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies