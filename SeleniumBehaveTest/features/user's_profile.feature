# Created by IgorSenkiv at 29/10/2019
Feature: check user's profile

  Scenario: user modifies personal user's data changing user's name, surname and email
    Given set up url address "login/index.php" and execute log in
    When user clicks on user's image profile on the left side bar
    And within the section "Dettagli dell'utente" user clicks on the button "modifica"
    And user clicks on "Annulla cambio email" and inserts user's firstname, last name, email"
    And user clicks on "Aggiornamento profilo" and confirm operation clicks on "Continua"
    Then user's firstname, surname and email should be changed