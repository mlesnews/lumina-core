# 11Labs SMS & Phone Calls Setup

**Date**: 1768546833.6839278

## Configuration Complete

11Labs has been configured for all SMS and phone call operations.

```json
{
  "11labs_config": {
    "api_version": "v1",
    "base_url": "https://api.elevenlabs.io/v1",
    "credentials": {
      "storage": "Azure Vault",
      "secrets": [
        "elevenlabs-api-key",
        "elevenlabs-voice-id-default",
        "elevenlabs-voice-id-sms",
        "elevenlabs-voice-id-phone"
      ]
    },
    "voices": {
      "default": {
        "description": "Default voice for general use",
        "voice_id": "stored_in_azure_vault",
        "settings": {
          "stability": 0.5,
          "similarity_boost": 0.75,
          "style": 0.0,
          "use_speaker_boost": true
        }
      },
      "sms_voice": {
        "description": "Voice for SMS reading and responses",
        "voice_id": "stored_in_azure_vault",
        "settings": {
          "stability": 0.6,
          "similarity_boost": 0.8,
          "style": 0.2,
          "use_speaker_boost": true
        }
      },
      "phone_voice": {
        "description": "Voice for phone call interactions",
        "voice_id": "stored_in_azure_vault",
        "settings": {
          "stability": 0.7,
          "similarity_boost": 0.85,
          "style": 0.3,
          "use_speaker_boost": true
        }
      }
    },
    "features": {
      "text_to_speech": true,
      "voice_cloning": false,
      "conversational_ai": true,
      "real_time_voice": true
    }
  },
  "sms_integration": {
    "description": "SMS processing with 11Labs voice integration",
    "use_cases": [
      "Read incoming SMS messages aloud",
      "Convert SMS to voice notifications",
      "Generate voice responses to SMS",
      "Voice-to-SMS conversion (speak to send SMS)"
    ],
    "workflow": {
      "incoming_sms": [
        "1. Receive SMS via webhook/API",
        "2. Process through SYPHON for intelligence",
        "3. Convert SMS text to speech using 11Labs",
        "4. Play audio notification or send to voice device",
        "5. Store in Holocron with voice metadata"
      ],
      "outgoing_sms": [
        "1. User speaks message (voice input)",
        "2. Transcribe speech to text (STT)",
        "3. Process through SYPHON",
        "4. Generate SMS response using 11Labs voice (optional preview)",
        "5. Send SMS via Twilio/API"
      ],
      "sms_voice_notifications": [
        "1. Detect priority SMS",
        "2. Generate voice alert using 11Labs",
        "3. Play on connected devices (Alexa, speakers, etc.)",
        "4. Log notification"
      ]
    },
    "n8n_integration": {
      "nodes": [
        "Webhook (SMS incoming)",
        "11Labs Text-to-Speech",
        "HTTP Request (play audio)",
        "SYPHON Process",
        "Holocron Store"
      ]
    },
    "voice_settings": {
      "sms_reading": {
        "voice": "sms_voice",
        "speed": 1.0,
        "pitch": 0.0,
        "add_pauses": true
      },
      "sms_notifications": {
        "voice": "sms_voice",
        "speed": 1.1,
        "pitch": 0.2,
        "add_urgency": true
      }
    }
  },
  "phone_calls": {
    "description": "Phone call handling with 11Labs voice AI",
    "incoming_calls": {
      "workflow": [
        "1. Receive incoming call (Twilio/API)",
        "2. Answer call automatically",
        "3. Use 11Labs for voice greeting",
        "4. Transcribe caller speech (STT)",
        "5. Process through SYPHON for intent",
        "6. Generate response using 11Labs TTS",
        "7. Speak response to caller",
        "8. Handle call routing/actions",
        "9. Store call transcript in Holocron"
      ],
      "features": {
        "auto_answer": true,
        "voice_greeting": true,
        "call_screening": true,
        "call_routing": true,
        "voicemail_transcription": true,
        "call_recording": true
      },
      "greeting_templates": {
        "default": "Hello, this is an automated assistant. How can I help you?",
        "business_hours": "Thank you for calling. This is an automated assistant. Please state your name and the reason for your call.",
        "after_hours": "Thank you for calling. We're currently outside business hours. Please leave a message and we'll get back to you."
      }
    },
    "outgoing_calls": {
      "workflow": [
        "1. Trigger outgoing call (schedule/event)",
        "2. Generate call script using AI",
        "3. Use 11Labs to create voice audio",
        "4. Place call via Twilio/API",
        "5. Play 11Labs voice message",
        "6. Listen for response (STT)",
        "7. Process response through SYPHON",
        "8. Generate follow-up using 11Labs",
        "9. Continue conversation or end call",
        "10. Store call record in Holocron"
      ],
      "use_cases": [
        "Appointment reminders",
        "Follow-up calls",
        "Information delivery",
        "Automated check-ins"
      ]
    },
    "voice_settings": {
      "phone_voice": {
        "voice": "phone_voice",
        "speed": 0.95,
        "pitch": 0.0,
        "stability": 0.7,
        "similarity_boost": 0.85
      },
      "conversational": {
        "enable_interruptions": true,
        "response_time": "real_time",
        "natural_pauses": true
      }
    },
    "integration": {
      "twilio": {
        "description": "Twilio for call handling",
        "webhook_url": "http://10.17.17.32:5678/webhook/11labs/phone",
        "credentials": "stored_in_azure_vault"
      },
      "11labs": {
        "api": "https://api.elevenlabs.io/v1",
        "conversational_ai": true,
        "real_time_voice": true
      }
    }
  },
  "n8n_workflows": {
    "sms_11labs_incoming": {
      "name": "SMS \u2192 11Labs Voice \u2192 Notification",
      "description": "Convert incoming SMS to voice using 11Labs",
      "trigger": {
        "type": "webhook",
        "url": "http://10.17.17.32:5678/webhook/sms/11labs",
        "method": "POST"
      },
      "nodes": [
        {
          "name": "Webhook",
          "type": "n8n-nodes-base.webhook",
          "parameters": {
            "path": "sms/11labs",
            "httpMethod": "POST"
          }
        },
        {
          "name": "Parse SMS",
          "type": "n8n-nodes-base.function",
          "parameters": {
            "functionCode": "const sms = $input.item.json;\nreturn [{\n  json: {\n    from: sms.from || sms.phone_number,\n    message: sms.body || sms.message,\n    timestamp: sms.timestamp || new Date().toISOString()\n  }\n}];"
          }
        },
        {
          "name": "11Labs TTS",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "url": "https://api.elevenlabs.io/v1/text-to-speech/{{ $env.ELEVENLABS_VOICE_ID_SMS }}",
            "method": "POST",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": true,
            "headerParameters": {
              "xi-api-key": "={{ $env.ELEVENLABS_API_KEY }}"
            },
            "sendBody": true,
            "bodyParameters": {
              "text": "={{ 'New message from ' + $json.from + '. ' + $json.message }}",
              "model_id": "eleven_multilingual_v2",
              "voice_settings": {
                "stability": 0.6,
                "similarity_boost": 0.8
              }
            },
            "options": {
              "response": {
                "response": {
                  "responseFormat": "file"
                }
              }
            }
          }
        },
        {
          "name": "Play Audio",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "url": "http://localhost:8000/api/audio/play",
            "method": "POST",
            "sendBody": true,
            "bodyParameters": {
              "audio": "={{ $binary.data }}"
            }
          }
        },
        {
          "name": "SYPHON Process",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "url": "http://localhost:8000/api/syphon/process",
            "method": "POST",
            "bodyParameters": {
              "content": "={{ $('Parse SMS').item.json.message }}",
              "source_type": "sms",
              "has_voice": true
            }
          }
        }
      ]
    },
    "phone_11labs_incoming": {
      "name": "Incoming Call \u2192 11Labs Voice AI",
      "description": "Handle incoming phone calls with 11Labs",
      "trigger": {
        "type": "webhook",
        "url": "http://10.17.17.32:5678/webhook/phone/11labs",
        "method": "POST"
      },
      "nodes": [
        {
          "name": "Twilio Webhook",
          "type": "n8n-nodes-base.webhook",
          "parameters": {
            "path": "phone/11labs",
            "httpMethod": "POST"
          }
        },
        {
          "name": "11Labs Conversational AI",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "url": "https://api.elevenlabs.io/v1/convai/conversation",
            "method": "POST",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "headerParameters": {
              "xi-api-key": "={{ $env.ELEVENLABS_API_KEY }}"
            },
            "bodyParameters": {
              "agent_id": "={{ $env.ELEVENLABS_AGENT_ID }}",
              "phone_number": "={{ $json.From }}"
            }
          }
        },
        {
          "name": "Call Transcription",
          "type": "n8n-nodes-base.function",
          "parameters": {
            "functionCode": "// Store call transcript\nconst call = $input.item.json;\nreturn [{\n  json: {\n    call_sid: call.CallSid,\n    from: call.From,\n    to: call.To,\n    transcript: call.TranscriptionText || '',\n    duration: call.CallDuration,\n    timestamp: new Date().toISOString()\n  }\n}];"
          }
        },
        {
          "name": "SYPHON Process",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "url": "http://localhost:8000/api/syphon/process",
            "method": "POST",
            "bodyParameters": {
              "content": "={{ $json.transcript }}",
              "source_type": "phone_call",
              "call_metadata": "={{ JSON.stringify($json) }}"
            }
          }
        }
      ]
    },
    "phone_11labs_outgoing": {
      "name": "Outgoing Call \u2192 11Labs Voice",
      "description": "Make outgoing calls with 11Labs voice",
      "trigger": {
        "type": "schedule",
        "cron": "0 9 * * *"
      },
      "nodes": [
        {
          "name": "Get Call List",
          "type": "n8n-nodes-base.function",
          "parameters": {
            "functionCode": "// Get list of calls to make\nreturn [{ json: { phone: '+1234567890', message: 'Your appointment reminder' } }];"
          }
        },
        {
          "name": "11Labs Generate Audio",
          "type": "n8n-nodes-base.httpRequest",
          "parameters": {
            "url": "https://api.elevenlabs.io/v1/text-to-speech/{{ $env.ELEVENLABS_VOICE_ID_PHONE }}",
            "method": "POST",
            "headerParameters": {
              "xi-api-key": "={{ $env.ELEVENLABS_API_KEY }}"
            },
            "bodyParameters": {
              "text": "={{ $json.message }}",
              "model_id": "eleven_multilingual_v2"
            }
          }
        },
        {
          "name": "Twilio Make Call",
          "type": "n8n-nodes-base.twilio",
          "parameters": {
            "operation": "makeCall",
            "to": "={{ $json.phone }}",
            "from": "={{ $env.TWILIO_PHONE_NUMBER }}",
            "url": "http://10.17.17.32:5678/webhook/twilio/play-audio"
          }
        }
      ]
    }
  },
  "uhura_integration": {
    "sms_channels": {
      "11labs_sms": {
        "id": "sms_11labs",
        "name": "SMS (11Labs Voice)",
        "provider": "11Labs",
        "n8n_node": "HTTP Request",
        "status": "configured",
        "features": [
          "SMS to voice conversion",
          "Voice SMS notifications",
          "Voice-to-SMS input"
        ]
      }
    },
    "voice_channels": {
      "11labs_phone": {
        "id": "phone_11labs",
        "name": "Phone Calls (11Labs)",
        "provider": "11Labs + Twilio",
        "n8n_node": "Twilio + HTTP Request",
        "status": "configured",
        "features": [
          "Incoming call handling",
          "Outgoing call automation",
          "Voice AI conversations",
          "Call transcription"
        ]
      }
    },
    "alert_configuration": {
      "voice_alerts": {
        "enabled": true,
        "provider": "11Labs",
        "triggers": [
          "priority_sms",
          "incoming_call",
          "critical_message"
        ],
        "voice_settings": {
          "voice_id": "sms_voice",
          "speed": 1.1,
          "urgency_tone": true
        }
      }
    }
  },
  "summary": {}
}
```
