# Created by IgorSenkiv at 14/11/2019
Feature: Privacy and policy feature

  Scenario: user denies OPTIONAL agreement policy through user's profile
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    When click on user's image profile on the left side bar
    And scroll down the page at the section "Administration" and click on the link "Site policy consents"
    And click on the name of policy "Albo Expert Teacher (non è obligatorio il consenso)"
#as select we can use "Do il consenso" or "Nego il consenso"
    And select alternative choice for optional privacy "Do il consenso" and press invia
    Then user should be redirected to the personal dashboard

  Scenario: user denies MANDATORY agreement policy through user's profile
   Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
   When click on user's image profile on the left side bar
   And scroll down the page at the section "Administration" and click on the link "Site policy consents"
   And click on the name of policy "Privacy policy_DEMO ( è obligatorio il consenso)"
#as select we can use "Do il consenso" or "Nego il consenso"
   And select alternative choice for mandatory privacy "Nego il consenso" and press invia
   Then should appear pup-up massage with header "Consenso ritirato"
   And approve consent withheld clicking on the button "Elimina la mia autenticazione"
   Then user should be logged out end redirected on the page "et.erickson.it: Login al sito"
   When execute login with credentials "i.senkiv" and "Totara_2019"
   Then should be appeared mandatory policy "Privacy policy_DEMO ( è obligatorio il consenso)"