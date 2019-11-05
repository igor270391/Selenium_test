# Created by IgorSenkiv at 29/10/2019
Feature: check user's profile

  Scenario: user modifies personal user's data changing user's name, surname and email
    Given set up url address "login/index.php" and execute log in
    When user clicks on user's image profile on the left side bar
    And within the section "Dettagli dell'utente" user clicks on the button "modifica"
    And user inserts "user's firstname, last name, email"
    And clicks on "Aggiornamento profilo"
    Then user's firstname, surname should be changed and email adress should have link "Annulla cambio email"