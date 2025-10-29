import { z } from 'zod';

/**
 * Signup request validation schema
 * Implements password complexity requirements from standards.md
 * [Source: docs/architecture.md#data-models, docs/standards.md#password-security]
 */
export const signupSchema = z.object({
  email: z
    .string()
    .email('Email format is invalid')
    .max(255, 'Email must be less than 255 characters'),

  password: z
    .string()
    .min(8, 'Password must be at least 8 characters')
    .regex(/[A-Z]/, 'Password must contain at least 1 uppercase letter')
    .regex(/[a-z]/, 'Password must contain at least 1 lowercase letter')
    .regex(/[0-9]/, 'Password must contain at least 1 number')
    .regex(/[!@#$%^&*]/, 'Password must contain at least 1 special character (!@#$%^&*)')
});

export type SignupRequest = z.infer<typeof signupSchema>;
