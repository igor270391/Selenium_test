# Created by IgorSenkiv at 20/09/2019
Feature: check lateral menu when the user has already logged

   Scenario: login in one step
    Given set up url address "login/index.php" and execute log in


  Scenario: user check if the right sidebar is accessible and navigable
    Given set up url address "login/index.php" and execute log in
    When user clicks on the button on the right corner of the sidebar to close and reopen it
    And scroll down the right sidebar
    And scroll down the content of the page
    Then the sidebar and content of the page should be scrolled

  Scenario: user opens own user's profile from right sidebar
    Given set up url address "login/index.php" and execute log in
    When user navigates to the right side bar
    And clicks on the user's image of "Profilo Personale"
    Then the user profile pages "DETTAGLI DELL'UTENTE" should be opened

  Scenario: check if user may opens user form with detail personality data
    Given set up url address "login/index.php" and execute log in
    When clicks on the user's image of "Profilo Personale"
    And finds the button "modifica" and clicks on it
    Then the page of user's personality details data should be opened

  Scenario: user opens own profile and changes user's name, surname and email
    Given set up url address "login/index.php" and execute log in
    When user opens own profile and clicks "modifica"
    And user insert "Nome", "Cognome" and "Indirizzo email"
    And clicks on "Aggiornamento profilo"
    Then user's profile should be updated with news data


