# Created by IgorSenkiv at 1/21/2020
Feature: mtauto_comletion
  this feature gives confirm that activity has completed

  Scenario: appear green check item next to activity when user satisfies completion criteria of activity will
    Given set up url address "login/index.php" and execute login typing "i.senkiv" and "Totara_2019" and agree site policies
    And go into the course "/course/view.php?id=17"
    Then expanding the drop down menu of Video Content, the activity with "id=182" shouldn't be completed
#    When click on the title "What is a Learning Management System" of activity and perform playing video
#    Then should appear green check next to the tittle of video content activity