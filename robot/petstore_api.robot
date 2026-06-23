*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${BASE_URL}     https://petstore.swagger.io/v2
${PET_ID}       ${87654321}

*** Test Cases ***

Get Pets By Status Returns List
    Create Session    petstore    ${BASE_URL}
    ${response}=      GET On Session    petstore    /pet/findByStatus    params=status=available
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=          Set Variable    ${response.json()}
    Should Not Be Empty    ${body}

Create Pet And Verify
    Create Session    petstore    ${BASE_URL}
    ${payload}=       Create Dictionary    id=${PET_ID}    name=RFDog    status=available
    ${response}=      POST On Session    petstore    /pet    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    ${name}=          Get From Dictionary    ${response.json()}    name
    Should Be Equal    ${name}    RFDog

Get Created Pet By Id
    Create Session    petstore    ${BASE_URL}
    ${response}=      GET On Session    petstore    /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    ${status}=        Get From Dictionary    ${response.json()}    status
    Should Be Equal    ${status}    available

Delete Pet
    Create Session    petstore    ${BASE_URL}
    ${response}=      DELETE On Session    petstore    /pet/${PET_ID}    expected_status=any
    Should Be True    ${response.status_code} in [200, 404]
