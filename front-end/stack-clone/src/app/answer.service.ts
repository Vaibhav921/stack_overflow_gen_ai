import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Answer {
  title: string;
  body: string;
}

@Injectable({
  providedIn: 'root'
})
export class AnswerService {
  private apiUrl = 'http://localhost:5000/answers'; // replace with your backend URL

  constructor(private http: HttpClient) {}

  getAnswers(question: string, useAISort: boolean): Observable<Answer[]> {
    return this.http.post<Answer[]>(this.apiUrl, {
      question: question,
      use_ai_sort: useAISort
    });
  }
}