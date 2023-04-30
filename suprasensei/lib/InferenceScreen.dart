import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class InferencePage extends StatefulWidget {
  @override
  _InferencePageState createState() => _InferencePageState();
}

class _InferencePageState extends State<InferencePage> {
  final TextEditingController _symptomsController = TextEditingController();
  String _solution = '';

  Future<void> _submitSymptoms() async {
    final String apiUrl = 'http://localhost:5000/api/infer';
    final response = await http.post(
      Uri.parse(apiUrl),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(
          <String, dynamic>{'symptoms': _symptomsController.text.split(',')}),
    );
    final responseData = jsonDecode(response.body);
    setState(() {
      _solution = responseData['solution'] ?? 'No solution found.';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text('Car Diagnostic Expert System'),
        backgroundColor: Color(0XFF6C1D22),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextField(
                controller: _symptomsController,
                decoration: InputDecoration(
                  hintText: 'Enter symptoms separated by commas',
                  hintStyle: TextStyle(color: Colors.grey),
                  border: OutlineInputBorder(
                      borderSide: BorderSide(
                    color: Color(0XFF6C1D22),
                  )),
                ),
              ),
              SizedBox(height: 16),
              Container(
                height: 40,
                width: 200,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    primary: Color(0XFF6c1D22) // background color
                    , // text color
                  ),
                  onPressed: _submitSymptoms,
                  child: Text(
                    'Submit Symptoms',
                    style: TextStyle(fontSize: 15),
                  ),
                ),
              ),
              SizedBox(height: 16),
              Text(
                'Solution: $_solution',
                style: TextStyle(fontSize: 20),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
