# Created by IgorSenkiv at 29/10/2019
Feature: check user's profile

    Scenario: user opens own user's within left sidebar
    Given set up url address "login/index.php" and execute log in
    When user clicks on user's image profile on the left side bar
    And within the section "Dettagli dell'utente" user clicks on the button "modifica"
    Then the edit page of user's personality details data should be opened

  Scenario: user modifies personal user's data changing user's name, surname and email
    Given set up url address "login/index.php" and execute log in
    When user clicks on user's image profile on the left side bar
    And within the section "Dettagli dell'utente" user clicks on the button "modifica"
    And user insert "Test"
#    And clicks on "Aggiornamento profilo"
#    Then user's profile should be updated with news data, "User", "t.user@nomil.invalid"