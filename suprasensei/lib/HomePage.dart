import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:suprasensei/InferenceScreen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xff131315),
      body: Column(
        children: [
          SizedBox(
            height: 60,
          ),
          Image.asset("./assets/car.jpg"),
          SizedBox(
            height: 200,
          ),
          GestureDetector(
            onTap: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => InferencePage()));
            },
            child: Container(
              height: 60,
              width: 250,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20),
                color: Color(0XFF6C1D22),
              ),
              child: Center(
                  child: Text(
                'Diagnose your car',
                style: TextStyle(
                  fontSize: 25,
                  color: Color(0xff131315),
                ),
              )),
            ),
          )
        ],
      ),
    );
  }
}
