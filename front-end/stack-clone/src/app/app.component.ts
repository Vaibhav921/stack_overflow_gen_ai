import { Component } from '@angular/core';
import { AnswerService, Answer } from './answer.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  question: string = '';
  answers: Answer[] = [];
  useAISort: boolean = false;
  loading: boolean = false;

  constructor(private answerService: AnswerService) {}

  search() {
    this.loading = true;
    this.answerService.getAnswers(this.question, this.useAISort).subscribe({
      next: (data) => {
        this.answers = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error fetching answers', err);
        this.loading = false;
      }
    });
  }

  toggleAISort() {
    this.useAISort = !this.useAISort;
    if (this.question.trim() !== '') {
      this.search();
    }
  }
}