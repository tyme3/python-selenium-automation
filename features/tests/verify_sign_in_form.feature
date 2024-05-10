# Created by Dimitri at 5/10/2024
Feature: Verify Sign In Form

  Scenario: Verify sign-in form for logged out user
    Given Open Target main page
    When  Click Sign In
    When  Click Sign In from the right side navigation menu
    Then  Verify Sign In form is opened
