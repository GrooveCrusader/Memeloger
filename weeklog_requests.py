'''
This module provides methods to get template requests, used to alter the spreadsheet
'''

ROW_MARGIN = 20

def name_headers(service, spreadsheet_id):
    request = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {
                "majorDimension": "ROWS",
                "range": "A1:G1",
                "values": [
                    [
                        'Case ID',
                        'Title',
                        'Category',
                        'Last Updated',
                        'Replies',
                        '',
                        'Other tasks'
                    ]
                ]
            }
        ]
    }
    return service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=request).execute()

def add_sheet(service, spreadsheet_id, sheet_title):
    request = {
        'requests': [
            {
                'addSheet': {
                    "properties": {
                        'title': sheet_title,
                        'index': 0,
                        'gridProperties': {
                            'rowCount': 10,
                            'columnCount': 10,
                            'frozenRowCount': 1
                        }
                    }
                }
            }
        ]
    }
    return service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=request).execute()

def apply_formatting(service, spreadsheet_id, sheet_id, categories):
    request = {
        'requests': [
            {
                # Gradient background for Replies column
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [
                            {
                                "sheetId": sheet_id,
                                "startRowIndex": 1,                                        
                                "startColumnIndex": 4,
                                "endColumnIndex": 5
                            }
                        ],
                        "gradientRule": {
                            "minpoint": {
                                "color": {
                                    "red": 1.0,
                                    "green": 1.0,
                                    "blue": 1.0
                                },
                                "type": "NUMBER",
                                "value": "0"
                            },
                            "midpoint": {
                                "color": {
                                    "red": 0.9,
                                    "green": 0.7,
                                    "blue": 0.7
                                },
                                "type": "NUMBER",
                                "value": "6"
                            },
                            "maxpoint": {
                                "color": {
                                    "red": 0.9
                                },
                                "type": "MAX"
                            },
                        }
                    },
                    "index": 0
                }
            },
            {
                # Background change for Category column cells with value "Converted"
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [
                            {
                                "sheetId": sheet_id,
                                "startColumnIndex": 2,
                                "endColumnIndex": 3
                            }
                        ],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [
                                    {
                                        "userEnteredValue": categories['Converted'].name
                                    }
                                ]
                            },
                            "format": {
                                "backgroundColor": {
                                    "red": 0.75,
                                    "green": 0.85,
                                    "blue": 0.85
                                }
                            }
                        }
                    },
                    "index": 0
                }
            },
            {
                # Background change for Category column cells with value "Submitted"
                "addConditionalFormatRule": {
                    "rule": {
                        "ranges": [
                            {
                                "sheetId": sheet_id,
                                "startColumnIndex": 2,
                                "endColumnIndex": 3
                            }
                        ],
                        "booleanRule": {
                            "condition": {
                                "type": "TEXT_EQ",
                                "values": [
                                    {
                                        "userEnteredValue": categories['Submitted'].name
                                    }
                                ]
                            },
                            "format": {
                                "backgroundColor": {
                                    "red": 0.9,
                                    "green": 0.8,
                                    "blue": 0.65
                                }
                            }
                        }
                    },
                    "index": 0
                }
            },
            {
                # Header formatting
                "repeatCell": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 0,
                        "endRowIndex": 1
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {
                                "red": 0.0,
                                "green": 0.0,
                                "blue": 0.0
                            },
                            "horizontalAlignment": "CENTER",
                            "textFormat": {
                                "foregroundColor": {
                                    "red": 1.0,
                                    "green": 1.0,
                                    "blue": 1.0
                                },
                                "fontSize": 12,
                                "bold": True
                            }
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
                }
            },
            {
                # Date format for Last Updated column
                "repeatCell": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 1,
                        "startColumnIndex": 3,
                        "endColumnIndex": 4
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "numberFormat": {
                                "type": "DATE_TIME",
                                "pattern": "dddd, yyyy-mm-dd"
                            }
                        }
                    },
                    "fields": "userEnteredFormat.numberFormat"
                }
            },
            {
                # Setting sheet index to 0 and freezing 1st row
                'updateSheetProperties': {
                    'properties': {
                        'sheetId': sheet_id,
                        'index': 0,
                        'gridProperties': {
                            'frozenRowCount': 1
                        }
                    },
                    'fields': 'index,gridProperties.frozenRowCount'
                }
            }
        ]
    }
    return service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=request).execute()