/**
 * Session Context Injector Middleware
 * Retrieves temporal facts and formats concise sub-15ms system prompt context.
 */

export interface FactRecord {
  entity: string;
  relation: string;
  value: string;
  retention: number;
}

export class SessionContextInjector {
  public static formatPromptContext(facts: FactRecord[]): string {
    if (!facts.length) return '';
    const lines = facts.map(f => `- [${f.entity}] ${f.relation}: ${f.value} (conf: ${(f.retention * 100).toFixed(0)}%)`);
    return `### Persistent Episodic Memory Context:
${lines.join('
')}
`;
  }
}
