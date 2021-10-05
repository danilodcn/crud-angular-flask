import { Component, OnInit, ViewChild } from '@angular/core';


import { Alunos } from '../models/alunos';


@Component({
  selector: 'app-alunos',
  templateUrl: './alunos.component.html',
  styleUrls: ['./alunos.component.scss']
})
export class AlunosComponent implements OnInit {

  public alunos: Alunos[] = [
    {_id: '1', nome: 'Danilo Nascimento', numero: "34", turma: "Calculo IV", curso_hab: "Engenharia Elétrica"}
  ];

  public displayedColumns = ["nome", "numero", "turma", "curso_hab"];

  constructor() {}

  ngOnInit(): void {
    
  }

}
