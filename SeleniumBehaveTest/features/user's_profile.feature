# Created by IgorSenkiv at 29/10/2019
Feature: check user's profile

    Scenario: modify user's profile data changing firstname, lastname and email
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    And click on user's image profile on the left side bar
    And within the section "Dettagli dell'utente" click on "modifica"
    When click on the link "Annulla cambio email" and insert user's firstname, last name, email"
    And click on "Aggiornamento profilo" and carry out modification clicking on "Continua"
    Then user's firstname, surname and email should be changed