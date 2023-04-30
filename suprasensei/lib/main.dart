import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:suprasensei/HomePage.dart';
import 'package:suprasensei/InferenceScreen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(debugShowCheckedModeBanner: false, home: HomeScreen());
  }
}
