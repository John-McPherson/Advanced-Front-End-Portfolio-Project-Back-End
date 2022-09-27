# **Testing** 

* [Functionality Testing](#functionality-testing)
* [Automated Testing](#automated-testing)
* [Bug Fixes](#bug-fixes)
* [Known Bugs](#known-bugs)


## Functionality Testing

As part of my testing profile I created test plan for manual testing. This way I could ensure that all functionality was working as expected. Whenever I would make a new version of the site live I would carry out the following tests before deploying the site

### Logged out

#### Projects 

1. Check to see that logout users can list projects
2. Check to make sure that logout users cannot add new projects
3. Check to see that logged out users cannot access individual projects. 
4. Check to see that the is_owner field reads false. 

#### Pages

1. Check to see that logout users can list pages
2. Check to make sure that logout users cannot add new pages
3. Check to see that logged out users can filter their pages. 
4. Check to see that a logged out user cannot post new pages. 
5. Check to see that the is_owner field reads false. 

#### Comments

1. Check to see that logout users can list pages
2. Check to see that users can see individual comments
3. Check to see that the is_owner field reads false. 

#### Profiles

1. Check to see that logout users can list profiles
2. Check to see that users can see individual comments
3. Check to see that logged out users can filter profiles. 
4. Check to see that users can see individual profiles
5. Check to see that the is_owner field reads false. 

### Create super user and log in


#### Projects 

1. Check to make sure that user can add new projects
2. Check to see that users can see individual projects
3. Check to make sure that user can update new projects
4. Check to see that the is_owner field and is_collaborator reads true. 
5. Check to make sure that user can't update projects they dont own or aren't collaborators


#### Pages 

1. Check to make sure that user can add new comments
2. Check to see that users can see individual comments
3. Check to see that the is_owner field and is_collaborator reads true. 
4. Check to make sure that user can't update pages they dont own or aren't collaborators

#### Profiles

1. Check to make sure that user can update their profile
2. Check to make sure that user can't update other profiles
3. Check to see that they can delete their profiles. 
4. Check to see all content owned by their profile is deleted. 

## Automated Testing

I created automated tests for the project view so that I can test to ensure everything is working easliy. 


## Bug Fixes

During testing I discovered and fixed the following bugs; 

1. Fix typo causing image vaildation to throw errors on correct sized files when uploading profile pictures fixed in commit [3347e3](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/33473e3496c1871be9d8fa89d5d91baf0d179cb7)

2. Fix issue causing pages to display out of order on front end. Fixed in commits [cba71c0](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/cba71c0a3048b191c4c81d10c7f264ea1899c522), [35b4cf4](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/35b4cf47cc852a1d6baccde0521a189c95c5ca20), [8440dfa](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/8440dfaf93985c224e878e6ddd7e597f6903391a)

3. Fix issue with filters not working on pages in commit [d0b20e0](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/d0b20e0a394c6b3ee784ca5c81dbab82356e9bf7)

4. Fix issue causing logout view not working [178ff3b](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/178ff3b254ec9e03c05ab67d89a0e5a67d64848a), [cbfe458](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/cbfe4589a50f222df578912e34cbb8665e9dca42)

5. Fix issue with comment serialiser not outputting usable user data fixed in commit [a0b8909](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/a0b890937305c4586ba2eee27102036242a8878b)

6. fix issue causing single page view to not load fixed in commit [15a80b9](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/15a80b9ed92ec496b97b438bd73410049fb7adde)

7. fix typo causing deployment to fail [240b580](https://github.com/John-McPherson/Advanced-Front-End-Portfolio-Project-Back-End/commit/240b580233b0cb681bd808d811189761e509248f)

## Known Bugs

There are currently no known bugs. 



