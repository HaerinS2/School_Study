package com.example.example4;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;

public class MainActivity extends AppCompatActivity {

    EditText editText;
    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText = (EditText) findViewById(R.id.edittext);
        textView = (TextView) findViewById(R.id.textview);
        editText.addTextChangedListener(new TextWatcher() {
            String beforetext;
            public void beforeTextChanged(CharSequence s, int i, int i1, int i2) {
                beforetext = s.toString();
            }

            public void onTextChanged(CharSequence s, int i, int i1, int i2) {

            }

            public void afterTextChanged(Editable s) {
                int length = showBytes();
                if(length > 80) editText.setText(beforetext);
            }
        });
    }
    private int showBytes(){
        try {
            int length = editText.getText().toString().getBytes("EUC-KR").length;
            textView.setText(length + " / 80 Bytes");
            return length;
        }catch (UnsupportedEncodingException e){
            e.printStackTrace();
        }
        return -1;
    }
    public void onbuttonsend(View v){
        String s = editText.getText().toString();
        final Toast toast = Toast.makeText(getApplicationContext(), s, Toast.LENGTH_LONG);
        toast.show();
        editText.setText("");
    }
    public void onbuttonclose(View v){
        AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
        builder.setMessage("진짜 끔?");
        builder.setTitle("알림창인척 하는 알림장")
                .setCancelable(false)
                .setNegativeButton("No", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int i) {
                        dialog.cancel();
                    }
                })
                .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int i) {
                        finish();
                    }
                });
        AlertDialog alert = builder.create();
        alert.setTitle(("알림장인척 하는 알림창"));
        alert.show();
    }
}