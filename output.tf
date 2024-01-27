output "api_key_value" {
  value = aws_api_gateway_api_key.example.value
  description = "The value of the API key"
  sensitive = true
}


