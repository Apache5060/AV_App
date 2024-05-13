def get_css():
    # Use a raw string or escape the backslashes
    background_image = "url('https://1931032958.rsc.cdn77.org/wp-content/uploads/2017/11/Sonata-Software-achieves-AWS-Service-Delivery-Designations-for-Amazon-Elastic-Kubernetes-Service-and-Amazon-DynamoDB-1536x864.jpg')"

    # Or use forward slashes instead
    # background_image = "url('C:/Users/guru.km/OneDrive - Sonata Software/Desktop/document/Flask_creation/Sonata-Software-achieves-AWS-Service-Delivery-Designations-for-Amazon-DynamoDB-1536x864.jpg')"

    return f"""
    <style>
    body {{
        background-image: {background_image};
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #f4f4f9;
        color: #333; /* General text color for readability */
    }}
    .stTextArea, .stTextInput {{
        background-color: #ffffff;
        color: #333; /* Black text color */
        border: 1px solid #ccc; /* Subtle border */
    }}
    .stButton>button {{
        background-color: #31333F; /* Green button background */
        color: white; /* White button text */
        border: none;
        padding: 10px 24px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px; /* Rounded button corners */
        transition: background-color 0.3s ease; /* Smooth hover transition */
    }}
    .stButton>button:hover {{
        background-color:  #ffffff; /* Darker green shade on hover */
    }}
    </style>
    """
