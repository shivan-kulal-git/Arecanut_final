<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form fields
    $name = $_POST['form_name'];
    $email = $_POST['form_email'];
    $phone = $_POST['form_phone'];
    $subject = $_POST['form_subject'];
    $message = $_POST['form_message'];

    // Recipient email address
    $to = 'kritidavda@gmail.com';

    // Email subject
    $email_subject = "Contact Form Submission: $subject";

    // Email body
    $email_body = "You have received a new message from the user $name.\n\n".
                  "Here are the details:\n".
                  "Name: $name\n".
                  "Email: $email\n".
                  "Phone: $phone\n".
                  "Subject: $subject\n".
                  "Message:\n$message";

    // Email headers
    $headers = "From: $email\n";
    $headers .= "Reply-To: $email";

    // Send email
    if (mail($to, $email_subject, $email_body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Message could not be sent.";
    }
}
?>
