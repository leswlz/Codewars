*** Settings ***
Library  ../../Codewars/Libraries/Break_camelCase.py
Library  String

*** Variables ***

*** Keywords ***
Test Break camelCase
    [Arguments]  ${input_string}  ${expected_output_string}
    ${result_string}=  Solution  ${input_string}
    Check Equality  ${result_string}  ${expected_output_string}

*** Test Cases ***
Test Strings With Pre-computed Data
    [Template]  Test Break camelCase
        # input string |  expecting
        helloWorld                  hello World
        camelCase                   camel Case
        breakCamelCase              break Camel Case
        askEyeSayNextNumber         ask Eye Say Next Number
        workNounsNumberWork         work Nouns Number Work
        bigUseLife                  big Use Life
        askTime                     ask Time
        groupManCase                group Man Case
        goodBigHave                 good Big Have
        adjectivesGoodBadBeGreat    adjectives Good Bad Be Great
        sayHandManPlace             say Hand Man Place
        takeEarlyAbleWorld          take Early Able World
        lifeGetFactMake             life Get Fact Make
        problemGetSay               problem Get Say
        groupLeaveOldChildFew       group Leave Old Child Few
        nextBadOtherNewLook         next Bad Other New Look
        useVerbsLook                use Verbs Look
        eyeEarlyGet                 eye Early Get
        getSeem                     get Seem
        numberImportant             number Important
        handSaySeemDayLittle        hand Say Seem Day Little
        otherOwnGoodSee             other Own Good See
        worldManWomanTell           world Man Woman Tell
        highThinkOldTake            high Think Old Take
        doSmallDay                  do Small Day
        pointCompany                point Company
        littleBadSay                little Bad Say
        ownFindNext                 own Find Next
        badVerbsNouns               bad Verbs Nouns
        yearAdjectivesThingWorld    year Adjectives Thing World
        childDoGreatHaveGood        child Do Great Have Good
