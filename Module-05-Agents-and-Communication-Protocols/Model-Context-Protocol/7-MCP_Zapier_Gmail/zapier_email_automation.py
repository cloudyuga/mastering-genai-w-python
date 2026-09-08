from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables
ZAPIER_BEARER_TOKEN = os.getenv('ZAPIER_BEARER_TOKEN')

if not ZAPIER_BEARER_TOKEN:
    raise ValueError("ZAPIER_BEARER_TOKEN environment variable is required. Please add it to your .env file.")

def send_email_via_zapier(prompt, recipient_email, subject="Email from Python Script"):
    """
    Send an email using Zapier MCP integration after processing a prompt
    
    Args:
        prompt (str): The prompt to process/execute
        recipient_email (str): Email address to send to
        subject (str): Email subject line (optional)
    """
    
    client = OpenAI()
    
    try:
        # Create the email sending instruction
        email_instruction = f"""
        Send an email using Gmail with the following details:
        - To: {recipient_email}
        - Subject: {subject}
        - Body: {prompt}
        
        Use the Gmail: Send Email tool to send this email.
        """
        
        # Use the MCP integration similar to your original code
        response = client.responses.create(
            model="gpt-4",
            input=email_instruction,
            tool_choice="required",
            tools=[
                {
                    "type": "mcp",
                    "server_label": "zapier",
                    "server_url": "https://mcp.zapier.com/api/mcp/mcp",
                    "require_approval": "never",
                    "headers": {
                        "Authorization": f"Bearer {ZAPIER_BEARER_TOKEN}",
                    },
                }
            ],
        )
        
        print("Email sent successfully!")
        #print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return None

def send_email_with_generated_content(prompt, recipient_email, subject="Email from Python Script"):
    """
    Alternative method: Generate content first, then send email
    """
    client = OpenAI()
    
    try:
        # First generate email content based on the prompt
        content_instruction = f"""
        Based on this prompt: "{prompt}"
        Generate appropriate email content and then send it to {recipient_email} with subject "{subject}" using Gmail.
        """
        
        response = client.responses.create(
            model="gpt-4",
            input=content_instruction,
            tool_choice="required",
            tools=[
                {
                    "type": "mcp",
                    "server_label": "zapier",
                    "server_url": "https://mcp.zapier.com/api/mcp/mcp",
                    "require_approval": "never",
                    "headers": {
                        "Authorization": f"Bearer {ZAPIER_BEARER_TOKEN}",
                    },
                }
            ],
        )
        
        print("Email sent successfully!")
        #print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return None

def main():
    """
    Main function to get user input and send email
    """
    print("=== Gmail Send Email via Zapier MCP ===")
    
    # Get input from user
    prompt = input("Enter your prompt/message: ")
    recipient_email = input("Enter recipient email address: ")
    subject = input("Enter email subject (or press Enter for default): ").strip()
    
    if not subject:
        subject = "Email from Python Script"
    
    # Validate email input
    if not recipient_email or "@" not in recipient_email:
        print("Please enter a valid email address.")
        return
    
    if not prompt.strip():
        print("Please enter a valid prompt.")
        return
    
    print("\nChoose method:")
    print("1. Send prompt directly as email content")
    print("2. Generate email content based on prompt")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    # Send the email
    print(f"\nSending email to {recipient_email}...")
    
    if choice == "2":
        result = send_email_with_generated_content(prompt, recipient_email, subject)
    else:
        result = send_email_via_zapier(prompt, recipient_email, subject)
    
    if result:
        print("Operation completed successfully!")
    else:
        print("Failed to send email.")

# Alternative direct usage function
def send_email_direct(message, to_email, email_subject="Message"):
    """
    Direct function to send email - use this if you want to call it programmatically
    """
    return send_email_via_zapier(message, to_email, email_subject)

if __name__ == "__main__":
    # Example direct usage:
    # send_email_direct("Hello, this is a test message!", "recipient@example.com", "Test Email")
    
    # Or use interactive mode:
    main()