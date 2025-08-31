<?php

// Name of the CSV file
$file = 'data.csv';

// Fetch data from POST request
$ip = $_POST['ip'] ?? '';
$userAgent = $_POST['userAgent'] ?? '';
$screenResolution = $_POST['screenResolution'] ?? '';
$userLocation = $_POST['userLocation'] ? json_encode($_POST['userLocation']) : '';  // store as JSON string
$referrer = $_POST['referrer'] ?? '';
$userLanguage = $_POST['userLanguage'] ?? '';
$timeZoneOffset = $_POST['timeZoneOffset'] ?? '';
$cookies = $_POST['cookies'] ?? '';
$localStorageData = $_POST['localStorageData'] ?? '';
$connectionType = $_POST['connectionType'] ?? '';

// Check if file exists, if not, create the header
if (!file_exists($file)) {
    $header = ['IP', 'User Agent', 'Screen Resolution', 'User Location', 'Referrer', 'User Language', 'Time Zone Offset', 'Cookies', 'Local Storage Data', 'Connection Type'];
    $handle = fopen($file, 'a');
    fputcsv($handle, $header);
    fclose($handle);
}

// Append data to CSV
$data = [$ip, $userAgent, $screenResolution, $userLocation, $referrer, $userLanguage, $timeZoneOffset, $cookies, $localStorageData, $connectionType];
$handle = fopen($file, 'a');
fputcsv($handle, $data);
fclose($handle);

echo "Data saved successfully";

?>
