###file:feature/check title

Feature: Validating Sky News website

  Scenario: Validating Sky News website
    Given I launch Sky News website
    When I check for the browser tab's title
    Then it should return the title "The Latest News from the UK and Around the World | Sky News"
    Then I should see all categories
	Then Home category should be active
	When I click on Ocean Rescue
	Then I should see the correct header text