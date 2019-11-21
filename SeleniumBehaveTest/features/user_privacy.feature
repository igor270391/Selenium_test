# Created by IgorSenkiv at 14/11/2019
Feature: Privacy and policy functionality

  Scenario: user deny agreement policy from through user's profile
    Given set up url address "login/index.php" and execute login with credentials "i.senkiv" and "Totara_2019" and consent site policy
    When click on user's image profile on the left side bar
    And scroll down the page at the section "Administration" and click on the link "Site policy consents"
    And click on the names of the policies and select "Nego il consenso"
#    And press "Submit" and approve consent withheld clicking on the button "Elimina la mia autenticazione"
#    Then user should be logged out end redirected on the login page